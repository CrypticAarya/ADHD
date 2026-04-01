import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState(null);
  const [lesson, setLesson] = useState(null);

  const concept = "linear_equations";

  const loadQuestion = async () => {
    const res = await fetch(`http://localhost:8000/question/${concept}`);
    const data = await res.json();
    setQuestion(data);
    setLesson(null);
  };

  const answer = async (option) => {
    const correct = option === question.answer;

    const res = await fetch("http://localhost:8000/answer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        concept,
        correct,
      }),
    });

    const data = await res.json();

    if (data.breakpoint) {
      loadLesson(data.breakpoint);
    } else {
      alert("correct");
    }
  };

  const loadLesson = async (concept) => {
    const res = await fetch(`http://localhost:8000/lesson/${concept}`);
    const data = await res.json();
    setLesson(data.lesson);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>ConceptBridge</h1>

      <button onClick={loadQuestion}>Start</button>

      {question && !lesson && (
        <div>
          <h2>{question.q}</h2>

          {question.options.map((o) => (
            <button key={o} onClick={() => answer(o)}>
              {o}
            </button>
          ))}
        </div>
      )}

      {lesson && (
        <div>
          <h2>Micro Lesson</h2>
          <p>{lesson}</p>
          <button onClick={loadQuestion}>Retry</button>
        </div>
      )}
    </div>
  );
}

export default App;