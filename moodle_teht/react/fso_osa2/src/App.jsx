import { useState, useEffect, React } from "react";
import personService from "./services/personService";
import "./App.css";

const personStatus = (time, type, newName) => {
  const addedName = document.querySelector(".addedName");
  addedName.style.display = "block";
  if (type === "added") {
    addedName.innerHTML = `${newName} lisätty.`;
    addedName.style.border = "3px solid green";
  } else if (type === "updated") {
    addedName.innerHTML = `${newName} päivitetty.`;
    addedName.style.border = "3px solid green";
  } else if (type === "deleted") {
    addedName.innerHTML = `${newName} poistettu.`;
    addedName.style.border = "3px solid red";
  }

  setTimeout(() => {
    addedName.style.display = "none";
  }, time);
}

const addedPersonStyle = {
  display: "none",
  color: "black",
  border: "3px solid green",
  padding: "10px",
  margin: "10px",
  borderRadius: "5px",
  width: "fit-content",
  textAlign: "center",
  backgroundColor: "#f2f2f2",
};

const Persons = ({ persons, filter, setPersons }) => {
  const filteredPersons = persons.filter((person) =>
    person.name.toLowerCase().includes(filter.toLowerCase())
  );
  return (
    <div>
      <tr>
        <th>Nimi</th>
        <th>Puhelinumero</th>
        <th>Poista</th>
      </tr>
      {filteredPersons.map((person) => (
        <tr key={person.name}>
          <td>{person.name}</td>
          <td>{person.number}</td>
          {/* delete person */}
          <td>
            <button
              onClick={() => {
                if (window.confirm(`Poistetaanko ${person.name}?`)) {
                  console.log("delete", person.id);
                  personService.deletePerson(person.id).then((response) => {
                    console.log(response);
                    // update persons
                    personService.getAll().then((initialPersons) => {
                      setPersons(initialPersons);
                    });
                  });
                  personStatus(1500, "deleted", person.name);
                }
              }}
            >
              Poista
            </button>
          </td>
        </tr>
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

  //update persons every 3 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      personService.getAll().then((initialPersons) => {
        setPersons(initialPersons);
      });
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    // name validation
    if (persons.some((person) => person.name === newName)) {
      if (newName === undefined || newName === null || newName === "") {
        alert("Anna nimi");
        return;
      }

      // phone number validation
      if (newNumber === undefined || newNumber === null || newNumber === "") {
        alert("Anna puhelinnumero");
        return;
      }

      if (
        window.confirm(
          `${newName} on jo luettelossa, Haluatko korvata vanhan numeron uudella?`
        )
      ) {
        // find person id
        const person = persons.find((person) => person.name === newName);
        // update person
        personService
          .update(person.id, { name: newName, number: newNumber })
          .then((returnedPerson) => {
            setPersons(
              persons.map((person) =>
                person.id !== returnedPerson.id ? person : returnedPerson
              )
            );
          });
        setNewName("");
        setNewNumber("");
        personStatus(1500, "updated", newName);
        return;
      }
    }

    //regex for maching any number and - and space
    else if (newNumber.match(/^[0-9\s-]+$/) === null) {
      alert("Aseta oikea puhelinnumero");
      return;
    } else {
      // add new person to persons database db.json file using personService
      personService
        .create({ name: newName, number: newNumber })
        .then((returnedPerson) => {
          setPersons(persons.concat(returnedPerson));
        });

      setNewName("");
      setNewNumber("");
      personStatus(1500, "added", newName);
    }
  };

  return (
    <div>
      <h2>Puhelinluettelo</h2>
      <div>
        <Filter filter={filter} setFilter={setFilter} />
      </div>
      <br />
      <p className="addedName" style={addedPersonStyle}></p>
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
      <table>
        <Persons setPersons={setPersons} persons={persons} filter={filter} />
      </table>
    </div>
  );
};

export default App;
