const Header = (props) => {
  console.log(props);
  return (
      <h1>{props.course}</h1>
  );
};

// const Part = (props) => {
//   return (
//     <div>
//       <p>Part</p>
//     </div>
//   );
// };

const Content = (props) => {
  return (
    <div>
      <p>
        Name of Course: {props.parts[0].name} <br />
        Exercises: {props.parts[0].exercises}
      </p>
      <p>
        Name of Course: {props.parts[1].name} <br />
        Exercises: {props.parts[1].exercises}
      </p>
      <p>
        Name of Course: {props.parts[2].name} <br />
        Exercises: {props.parts[2].exercises}
      </p>
    </div>
  );
}

const Total = (props) => {
  return (
    <div>
      <p>
        Number of exercises:{" "}
        {props.parts[0].exercises +
          props.parts[1].exercises +
          props.parts[2].exercises}
      </p>
    </div>
  );
};

const App = () => {
    const course = "Half Stack application development";
    const parts = [
      {
        name: "Fundamentals of React",
        exercises: 10,
      },
      {
        name: "Using props to pass data",
        exercises: 7,
      },
      {
        name: "State of a component",
        exercises: 14,
      },
    ];

  return (
    <div>
      <Header course={course} />
      <Content parts={parts} />
      <Total parts={parts} />
    </div>
  );
};

export default App;

