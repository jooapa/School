const Course = ({ props }) => {
  return (
    <div>
      <Header type={"h1"} course={props[0].header} />
      <Header type={"h2"} course={props[0].name} />
      <Content parts={props[0].parts} />
      <Total parts={props[0].parts} />
      <Header type={"h2"} course={props[1].name} />
      <Content parts={props[1].parts} />
      <Total parts={props[1].parts} />
    </div>
  );
};

const Header = (props) => {
  console.log(props);
  if (props.type === "h1") return <h1>{props.course}</h1>;
    else if (props.type === "h2") return <h2>{props.course}</h2>;
};

const Content = (props) => {

    const partElements = props.parts.map((part) => (
        <Part key={part.id} parts={part} />
    ));

  return <div>{partElements}</div>;
};

const Part = (props) => {
  return (
    <div>
      <p>
        Name of Course: <b>{props.parts.name} </b>
        <br />
        Exercises: {props.parts.exercises}
      </p>
    </div>
  );
};

const Total = (props) => {
    // laskee tehävät yhteen riippuen kuinka monta tehtävää on
    const total = props.parts.reduce((sum, part) => sum + part.exercises, 0);
    return (
    <div>
      <b>total of {total} exercises</b>
    </div>
  );
};

export default Course;