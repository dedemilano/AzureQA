from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

endpoint = "https://logeiquenlp.cognitiveservices.azure.com/"
credential = AzureKeyCredential("256057747801451599969c8e82c1f9f9")
knowledge_base_project = "https://ca.indeed.com/?from=mobRdr"
deployment = "production"

def main():
    client = QuestionAnsweringClient(endpoint, credential)
    with client:
        question="How much job opportunity in machine learning?"
        output = client.get_answers(
            question = question,
            project_name=knowledge_base_project,
            deployment_name=deployment
        )
    print("Q: {}".format(question))
    print("A: {}".format(output.answers[0].answer))

if __name__ == '__main__':
    main()