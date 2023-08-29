import { useState } from 'react'
import './App.css'

const MuistiinPano = () => {
  const [tasks, setTasks] = useState([])
  const [task, setTask] = useState('')
  const [taskHeader, setTaskHeader] = useState('')
  const [taskHeaders, setTaskHeaders] = useState([])

  const addTask = () => {
    if (task === "") return;
    if (taskHeader === "") return;
    setTasks([...tasks, task]);
    setTask("");
    setTaskHeaders([...taskHeaders, taskHeader]);
    setTaskHeader("");
  };

  const removeTask = (index) => {
    const newTasks = [...tasks]
    const newTaskHeaders = [...taskHeaders]
    newTasks.splice(index, 1)
    newTaskHeaders.splice(index, 1)
    setTasks(newTasks)
    setTaskHeaders(newTaskHeaders)
  }

  const handleUpdate = (e, index) => {
    const newTasks = [...tasks]
    newTasks[index] = e.target.value
    setTasks(newTasks)
  }

  return (
    <div className="App">
      <h1>Tehtävälista</h1>
      {"Otsikko: "}
      <input
        type="text"
        value={taskHeader}
        onChange={(e) => setTaskHeader(e.target.value)}
      />
      <br />
      {"Tehtävä: "}
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <br />
      <button onClick={addTask}>Lisää</button>
      <div>
        <h2>Tehtävät</h2>
        <div className="MuistikorttiContainer">
          {tasks.map((task, index) => (
            <div className="Muistikortti" key={index}>
              <h3 contentEditable>{taskHeaders[index]}</h3>
              <p contentEditable>{task}</p>
              <button onClick={() => removeTask(index)}>Poista</button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <MuistiinPano />
    </div>
  );
}

export default App
