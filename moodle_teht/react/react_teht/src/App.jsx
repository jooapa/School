import { useState } from 'react'
import './App.css'

Laskuri = () => {
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
function App() {
  return (
    <div className="App">
      <Laskuri />
    </div>
  );
}

export default App
