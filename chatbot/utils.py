from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .models import FAQ


model = SentenceTransformer('all-MiniLM-L6-v2')


def get_best_answer(user_query):

    faqs = FAQ.objects.all()

    questions = [faq.question for faq in faqs]

    answers = [faq.answer for faq in faqs]

    embeddings = model.encode(questions)

    query_embedding = model.encode([user_query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )

    best_match_index = similarities.argmax()

    score = similarities[0][best_match_index]

    if score < 0.4:
        return "Sorry, I could not understand your question."

    return answers[best_match_index]