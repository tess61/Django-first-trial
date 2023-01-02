import './App.css';
import { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [studData, setStudData] = useState([])

  const fetch =() => {
    axios.get("http://127.0.0.1:8000/student/student-list/")
    .then((result) => setStudData(result.data))
    .then(err => console.log(err))
  }
  useEffect(()=>{
    fetch();
    },[])
  return (
    <div className="App">
      <header className="App-header">
      {studData.map((result) => 
        <div>
          <h3>Name: {result.studentName}</h3>
          <h3>Grade: {result.Grade}</h3>
        </div>
      )}
      </header>
    </div>
  );
}

export default App;
