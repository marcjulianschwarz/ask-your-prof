interface ServerResponse {
  answer: string;
  doc_ids: string[];
}

async function apiQuestion(question: string) {
  const response = await fetch(
    `http://127.0.0.1:5000/ask?question=${question}`
  );
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  const data = (await response.json()) as ServerResponse;
  return data;
}

function askQuestion() {
  let chatHistory = document.getElementById("chat-history") as HTMLDivElement;
  let questionEl = document.getElementById("chat") as HTMLInputElement;

  if (questionEl == null) {
    return;
  } else {
    let question = questionEl.value;
    let questionDiv = document.createElement("div");
    questionDiv.innerHTML = "<p class='user-chat'>" + question + "</p>";
    chatHistory.appendChild(questionDiv);

    apiQuestion(question)
      .then((data) => {
        var answer = data["answer"];

        var answerDiv = document.createElement("div");
        answerDiv.innerHTML = "<p class='ai-chat'>" + answer + "</p>";
        chatHistory.appendChild(answerDiv);

        var docIdsDiv = document.createElement("div");
        docIdsDiv.innerHTML = "<p>" + data["doc_ids"] + "</p>";
        chatHistory.appendChild(docIdsDiv);
      })
      .catch((error) => {
        console.error(
          "There has been a problem with your fetch operation:",
          error
        );
      });
    questionEl.value = "";
  }
}
