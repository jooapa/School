import { useState, useEffect, React } from "react";
import axios from "axios";
import personService from "./services/personService";



const Persons = ({ persons, filter }) => {
  const filteredPersons = persons.filter((person) =>
    person.name.toLowerCase().includes(filter.toLowerCase())
  );
  return (
    <div>
      {filteredPersons.map((person) => (
        <table>
          <tr key={person.name}>
            <td>{person.name} |</td>
            <td>{person.number}</td>
            {/* delete person */}
            <td>
              <button
                onClick={() => {
                  if (window.confirm(`Poistetaanko ${person.name}?`)) {
                    console.log("delete", person.id);
                    personService.deletePerson(person.id).then((response) => {
                      console.log(response);
                    });
                  }
                }}
              >
                Poista
              </button>
            </td>
          </tr>
        </table>
      ))}
    </div>
  );
};

const PersonForm = ({ props }) => {
  return (
    <form onSubmit={props.handleSubmit}>
      <div>
        Nimi:{" "}
        <input
          type="text"
          value={props.newName}
          onChange={(e) => props.setNewName(e.target.value)}
        />
        <br />
        Puhelinumero:{" "}
        <input
          type="text"
          value={props.newNumber}
          onChange={(e) => props.setNewNumber(e.target.value)}
        />
      </div>
      <div>
        <input type="submit" />
      </div>
    </form>
  );
};

const Filter = ({ filter, setFilter }) => {
  return (
    <div>
      Rajaa näytettäviä:{" "}
      <input type="text" onChange={(e) => setFilter(e.target.value)} />
    </div>
  );
};

const App = () => {
  const [persons, setPersons] = useState([]);
  const [newName, setNewName] = useState("");
  const [newNumber, setNewNumber] = useState();
  const [filter, setFilter] = useState("");

  // useEffect(() => {
  //   fetchData();

  //   const intervalId = setInterval(() => {
  //     fetchData();
  //   }, 2000);

  //   return () => clearInterval(intervalId);
  // }, []);

  // const fetchData = () => {
  //   axios
  //     .get("http://localhost:3001/persons")

  //     .then((response) => {
  //       setPersons(response.data);

  //       console.log(response);
  //     })

  //     .catch((error) => {
  //       console.error("Error fetching data:", error);
  //     });
  // };

    useEffect(() => {
      personService.getAll().then((initialPersons) => {
        setPersons(initialPersons);
      });
    }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    // name validation
    if (persons.some((person) => person.name === newName)) {
      if (newName === undefined || newName === null || newName === "") {
        alert("Anna nimi");
        return;
      }
      alert(`${newName} on jo luettelossa`);
      return;
    }

    //regex for maching any letter and space
    if (newName.match(/[\p{Letter}\p{Mark}]+/gu) === null) {
      alert("Aseta oikea nimi");
      return;
    }
    // phone number validation
    else if (newNumber === undefined || newNumber === null || newNumber === "") {
      alert("Anna puhelinnumero");
      return;
    }

    //regex for maching any number and - and space
    else if (newNumber.match(/^[0-9\s-]+$/) === null) {
      alert("Aseta oikea puhelinnumero");
      return;
    }
    else {
     // add new person to persons database db.json file using personService
      personService.create({ name: newName, number: newNumber }).then((returnedPerson) => {
        setPersons(persons.concat(returnedPerson));
      });
      
      setNewName("");
      setNewNumber("");
    }
    
  };

  return (
    <div>
      <h2>Puhelinluettelo</h2>
      <div>
        <Filter filter={filter} setFilter={setFilter} />
      </div>
      <h3>Lisää uusi</h3>
      <PersonForm
        props={{
          handleSubmit,
          newName,
          setNewName,
          newNumber,
          setNewNumber,
        }}
      />
      <h2>Numerot</h2>
      <Persons persons={persons} filter={filter} />
    </div>
  );
};

export default App;
