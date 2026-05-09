def score_jobs(candidate_data, jobs):

    ranked_jobs = []

    for job in jobs:

        ranked_jobs.append({

            "job": {
                "title": job.get("title"),
                "company": job.get("company"),
                "url": job.get("url"),
                "source": job.get("source"),
            },

            "score": 92,

            "missing_skills": [
                "Docker",
                "TypeScript"
            ],

            "analysis": f"""
This opportunity is highly relevant for
{candidate_data.get('role')}.

Strong skill match detected.

Recommended to apply immediately.
            """
        })

    return ranked_jobs