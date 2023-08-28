import { useState } from 'react'
import './App.css'

const Laskuri = () => {
  const [num, setNum] = useState(0)

  return (
    <div className="App">
      <h1>Interaktiivinen laskuri</h1>
      <p>{num}</p>
      <button onClick={() => setNum(num + 1)}>Lisää</button>
      <button onClick={() => setNum(num - 1)}>Vähennä</button>
    </div>
  )
}

const TehtäväLista = () => {
  const [tasks, setTasks] = useState([])
  const [task, setTask] = useState('')
  
  const addTask = () => {
    if (task === '') return
    setTasks([...tasks, task])
    setTask('')
  }

  const removeTask = (index) => {
    const newTasks = [...tasks]
    newTasks.splice(index, 1)
    setTasks(newTasks)
  }

  return (
    <div className="App">
      <h1>Tehtävälista</h1>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button onClick={addTask}>Lisää</button>
      
        {tasks.map((task, index) => (
          <p key={index}>
            <b>{task}</b> <button onClick={() => removeTask(index)}>Poista: {task}</button>
          </p>
        ))}
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <Laskuri />
      <TehtäväLista />
    </div>
  );
}

export default App
