import React,{useState} from 'react';
import axios from 'axios';
import './App.css';

function App() {
  let[start,setStart]=useState();
  let[end,setEnd]=useState();
  let[algorithm,setAlgorithm]=useState();
  const[primes,setPrimes]=useState([]);
  const[count,setCount]=useState(0);
  const[time_Elapsed,setTimeElapsed]=useState(0);

  let generatePrimes= async ()=>{
    try{
      const result = await axios.get(`http://127.0.0.1:8000/?start=${start}&end=${end}&algorithm=${algorithm}`);
      setPrimes(result.data.primes);
      setCount(result.data.count);
      setTimeElapsed(result.data.time_elapsed);
    }catch(error){
      alert(error);
    }
  };
  return (
    <div className="App">
      <header className="App-header">
        <h2>Prime Generator</h2>
        <label>Start:
        <input type='number' value={start} onChange={(e)=>setStart(e.target.value)}></input>
        </label>

        <label>End:
        <input type='number' value={end} onChange={(e)=>setEnd(e.target.value)}></input>
        </label>

        <label>Algorithm:
        <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
          <option value="">select</option>
          <option value="normal_method1">Normal Method 1</option>
          <option value="normal_method2">Normal Method 2</option>
          <option value="sieve_eratosthenes">Sieve of Eratosthenes</option>
          <option value="trial_division">Trial Division</option>
        </select>
        </label>

        <button onClick={generatePrimes}>Generate Primes</button>
        <hr></hr>
        <p>Total Count: {count}</p>
        <p>Time Elapsed: {time_Elapsed} milliseconds</p>
        <h3>Prime Numbers:</h3>
        <ul>
          {primes.map((prime, index) => (
            <li key={index}>{prime}</li>
          ))}
        </ul>
        
        
      </header>
    </div>
  );
}

export default App;
