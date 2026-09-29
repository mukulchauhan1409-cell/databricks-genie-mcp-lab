"""Minimal Genie One MCP validation client.

Authentication is obtained from the local Databricks CLI profile.
No access token is stored in this repository.

Prerequisites:
  databricks auth login --host https://<workspace-hostname> -p DEFAULT
  pip install -r requirements.txt
"""

import asyncio
import json
import subprocess
from typing import Any

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

PROFILE = "DEFAULT"
WORKSPACE_HOST = "https://<workspace-hostname>"
MCP_URL = f"{WORKSPACE_HOST}/ai-gateway/mcp-services/system.ai.genie_one_mcp"


def get_access_token() -> str:
    result = subprocess.run(
        ["databricks", "auth", "token", "-p", PROFILE, "--output", "json"],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)["access_token"]


async def ask_genie(question: str) -> dict[str, Any]:
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    timeout = httpx.Timeout(30.0, read=300.0)
    async with httpx.AsyncClient(headers=headers, timeout=timeout) as http_client:
        async with streamable_http_client(MCP_URL, http_client=http_client) as (
            read_stream,
            write_stream,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                ask = await session.call_tool("genie_ask", {"question": question})
                started = json.loads(ask.content[0].text)

                conversation_id = started["conversation_id"]
                response_id = started["response_id"]

                while True:
                    poll = await session.call_tool(
                        "genie_poll_response",
                        {
                            "conversation_id": conversation_id,
                            "response_id": response_id,
                        },
                    )
                    response = json.loads(poll.content[0].text)
                    status = response.get("status")

                    if status in {"completed", "failed", "incomplete"}:
                        return response

                    await asyncio.sleep(2)


async def main() -> None:
    questions = [
        "Which customer generated the most revenue?",
        "What are the top 3 orders by amount?",
        "What is the total revenue by region?",
    ]

    for question in questions:
        result = await ask_genie(question)
        print(f"\nQuestion: {question}")
        print(f"Status: {result.get('status')}")
        print(result.get("final_answer", "No final answer returned."))


if __name__ == "__main__":
    asyncio.run(main())
