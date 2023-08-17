import { useState } from "react";

const MostVotes = (props) => {
  let max = Math.max(...props.votes);
  let index = props.votes.indexOf(max);
  if (max === 0) {
    return <div>ei ole eniten ääniä saatua tarinaa</div>;
  }
  else {
    return (
      <div>
        {props.anecdotes[index]}
        <br />
        {max + " äänellä"}
      </div>
    );
  }
};

const App = () => {
  const anecdotes = [
    "If it hurts, do it more often.",
    "Adding manpower to a late software project makes it later!",
    "The first 90 percent of the code accounts for the first 90 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "Premature optimization is the root of all evil.",
    "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.",
    "Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blood tests when dianosing patients.",
    "The only way to go fast, is to go well.",
  ];

  const [selected, setSelected] = useState(0);
  const [votes, setVotes] = useState(Array(anecdotes.length).fill(0));
  let rndInt;

  function getRandomInt(max) {
    rndInt = Math.floor(Math.random() * max);
    setSelected(rndInt);
    return
  }

  return (
    <div>
      <h1>Päivän tarina</h1>
      {anecdotes[selected] + " "}
      <br />
      {"has " + votes[selected] + " votes"}
      <br />
      <button onClick={() => getRandomInt(anecdotes.length)}>
        Seuraava tarina
      </button>
      <button
        onClick={() => {
          setVotes(votes.map((vote, i) => (i === selected ? vote + 1 : vote)));
        }}
      >
        {" "}
        äänestä
      </button>

      <h1>Eniten ääniä saanut tarina</h1>
      <MostVotes anecdotes={anecdotes} votes={votes} />
    </div>
  );
  
};

export default App;