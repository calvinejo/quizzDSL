# React code stored in a .py file as plain text (not executable Python)

react_quiz_code = """
import { useState, useEffect } from "react";

export default function QuizDSL() {
  const questions = [
    {
      q: "Quel est l’objectif principal des prises de mesures DSL ?",
      options: [
        "Vérifier l’intégrité du tubing",
        "Optimiser la production surface",
        "Ajuster les modèles réservoirs",
        "Planifier un workover"
      ],
      answer: 2
    },
    {
      q: "Quand doit-on prendre des mesures ?",
      options: [
        "Uniquement en cas de baisse de production",
        "Quand le fond est accessible",
        "Uniquement si le slickline est dispo",
        "Une fois par an"
      ],
      answer: 1
    },
    {
      q: "Au-delà de combien de mois doit-on reprendre une mesure ?",
      options: ["3 mois", "4 mois", "5 mois", "6 mois"],
      answer: 3
    },
    {
      q: "Dans quel sens enregistrer les données ?",
      options: ["Bas vers haut", "Haut vers bas", "Peu importe", "En alternance"],
      answer: 1
    },
    {
      q: "Pourquoi du haut vers le bas ?",
      options: [
        "Pour faciliter l’analyse G&G",
        "Car la pression surface est stable",
        "Pour réchauffer progressivement le capteur",
        "Pour éviter les erreurs humaines"
      ],
      answer: 2
    }
  ];

  const [current, setCurrent] = useState(0);
  const [score, setScore] = useState(0);
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);
  const [timeLeft, setTimeLeft] = useState(300); // 5 minutes

  useEffect(() => {
    if (finished) return;
    if (timeLeft <= 0) {
      setFinished(true);
      return;
    }
    const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
    return () => clearTimeout(timer);
  }, [timeLeft, finished]);

  function submitAnswer() {
    if (selected === null) return;

    if (selected === questions[current].answer) {
      setScore(score + 1);
    }

    if (current + 1 < questions.length) {
      setCurrent(current + 1);
      setSelected(null);
    } else {
      setFinished(true);
    }
  }

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;

  return (
    <div className="p-6 max-w-xl mx-auto space-y-4">
      <h1 className="text-2xl font-bold text-center">Quiz DSL - Interactif</h1>
      {!finished && (
        <div className="text-center text-lg font-semibold">
          Temps restant : {minutes}:{seconds.toString().padStart(2, "0")}
        </div>
      )}

      {!finished ? (
        <div className="space-y-4">
          <h2 className="text-lg font-semibold">
            Question {current + 1}/{questions.length}
          </h2>
          <p>{questions[current].q}</p>

          <div className="space-y-2">
            {questions[current].options.map((opt, i) => (
              <button
                key={i}
                onClick={() => setSelected(i)}
                className={`w-full p-2 rounded-xl border shadow-sm text-left ${
                  selected === i ? "bg-blue-200" : "bg-white"
                }`}
              >
                {opt}
              </button>
            ))}
          </div>

          <button
            onClick={submitAnswer}
            className="w-full py-2 bg-blue-600 text-white rounded-xl mt-4"
          >
            Valider
          </button>
        </div>
      ) : (
        <div className="text-center space-y-4">
          <h2 className="text-xl font-bold">Quiz terminé !</h2>
          <p className="text-lg">Score : {score} / {questions.length}</p>
          <p className="text-md">Temps écoulé ou questions terminées.</p>
        </div>
      )}
    </div>
  );
}
"""