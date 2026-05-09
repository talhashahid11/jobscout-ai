from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_jobs(candidate_data):

    role = candidate_data.get(
        "role",
        "Software Engineer"
    )

    # SHORT QUERY ONLY

    query = f"""
    latest remote {role} jobs
    official company careers
    """

    try:

        response = client.search(
            query=query,
            search_depth="basic",
            max_results=6
        )

        jobs = []

        for result in response.get("results", []):

            jobs.append({

                "title": result.get(
                    "title",
                    role
                ),

                "company": "Verified Company",

                "url": result.get(
                    "url",
                    "#"
                ),

                "content": result.get(
                    "content",
                    ""
                ),

                "source": "AI Search"
            })

        return jobs

    except Exception as e:

        print("SEARCH ERROR:", e)

        # FALLBACK JOBS

        return [

            {
                "title": "Laravel Developer",
                "company": "TechNova",
                "url": "https://larajobs.com",
                "content": "Remote Laravel role",
                "source": "Fallback"
            },

            {
                "title": "Full Stack Developer",
                "company": "PixelSoft",
                "url": "https://remoteok.com",
                "content": "Remote Full Stack role",
                "source": "Fallback"
            }

        ]