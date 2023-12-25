export interface TextDocument {
  id: string;
  content: string;
}

export interface ServerResponse {
  answer: string;
  docs: TextDocument[];
}

export async function askQuestion(question: string) {
  const response = await fetch(
    "http://127.0.0.1:5000/ask?question=" + question
  );
  const data = await response.json();
  const serverResponse: ServerResponse = data;
  return serverResponse;
}
