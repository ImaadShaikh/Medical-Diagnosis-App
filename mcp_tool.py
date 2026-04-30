from mcp.server.fastmcp import FastMCP
from functions.symptom_extractor import extract_symptom
from functions.diagnosis_symptoms import get_diagnosis
from functions.pubmed_articles import fetch_pubmed_articles_with_metadata
from functions.summarize_pubmed import summarize_text


mcp = FastMCP('Clinisight AI')


@mcp.tool()
async def Clinisight_ai(symptom_text):

    symptom = extract_symptom(symptom_text)

    diagnosis_result = get_diagnosis(symptom)

    pubmed_article = fetch_pubmed_articles_with_metadata(" ".join(symptom))

    if not pubmed_article:
        summary = "No articles found"
    else:
        articles_text = " ".join([
        (a["title"] + " " + a["abstract"])[:200]
        for a in pubmed_article
    ])
    summary = summarize_text(articles_text)

    return {
        "symptom": symptom,
        "diagnosis": diagnosis_result,
        "pubmed_summary": summary
    }


if __name__ == "__main__":
    mcp.run(transport = "stdio")