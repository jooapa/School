import { useState } from "react";

const Persons = ({ persons, filter }) => {
  const filteredPersons = persons.filter((person) =>
    person.name.toLowerCase().includes(filter.toLowerCase())
  );
  return (
    <div>
      {filteredPersons.map((person) => (
        <p key={person.name}>
          {person.name} {person.number}
        </p>
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
  const [persons, setPersons] = useState([{ name: "Arto Hellas", number: "040-1231244" }]);
  const [newName, setNewName] = useState("");
  const [newNumber, setNewNumber] = useState();
  const [filter, setFilter] = useState("");

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
    if (newName.match(/^[A-Za-z\s]+$/) === null) {
      alert("Aseta oikea nimi");
      return;
    }
    // phone number validation
    if (newNumber === undefined || newNumber === null || newNumber === "") {
      alert("Anna puhelinnumero");
      return;
    }

    //regex for maching any number and - and space
    if (newNumber.match(/^[0-9\s-]+$/) === null) {
      alert("Aseta oikea puhelinnumero");
      return;
    }
    
    setPersons([...persons, { name: newName, number: newNumber }]);

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
