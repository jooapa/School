import { useState } from "react";

const Statistics = (props) => {
  //addFeedback lisää arvoja muuttujiin, jotka ovat propsina tässä komponentissa
  const {good, neutral, bad} = props;

  if (good === 0 && neutral === 0 && bad === 0) {
    return(
      <div> No feedback given</div>
    ) 
  }
  else {
    return(
      <div>
      <tr>
      <li>
      <StatisticLine text="good" value = {good} />
      </li><li>
      <StatisticLine text="neutral" value = {neutral} />
      </li><li>
      <StatisticLine text="bad" value = {bad} />
      </li><li>
      <StatisticLine text="all" value = {bad + neutral + good} />
      </li><li>
      <StatisticLine text="average" value = {(good - bad) / (bad + neutral + good)} />
      </li><li>
      <StatisticLine text="positive" value = {good / (bad + neutral + good) * 100 + " %"} />
      </li>
      </tr>
      </div>
    )
  } 
  
}

const StatisticLine = (props) => {
  return (
    <div>
      <p>{props.text} {props.value}</p>
    </div>
  );
};

const Header = (props) => {
  return (
      <h2>{props.header}</h2>
  );
};


const App = () => {
  // tallenna napit omaan tilaansa
  const [good, setGood] = useState(0);
  const [neutral, setNeutral] = useState(0);
  const [bad, setBad] = useState(0);

  //lisää muutujiin arvoja useState hookin avulla
  function addFeedback(state) {
    if (state === "good") {
      setGood(good + 1);
    }
    if (state === "neutral") {
      setNeutral(neutral + 1);
    }
    if (state === "bad") {
      setBad(bad + 1);
    }
  }

  
  return (
    <div>
      <Header header={"give feedback"} />
      <br />
      <button onClick={() => addFeedback("good")}>good</button>
      <button onClick={() => addFeedback("neutral")}>neutral</button>
      <button onClick={() => addFeedback("bad")}>bad</button>
      <Header header={"statistics"} />
      <Statistics good={good} neutral={neutral} bad={bad}/>
    </div>
  );
};

export default App;
