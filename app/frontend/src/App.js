import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000';

function App() {
  const [patients, setPatients] = useState([]);
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [disease, setDisease] = useState('');
  const [priority, setPriority] = useState(false);
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchPatients();
  }, []);

  const fetchPatients = async () => {
    try {
      const response = await axios.get(`${API_URL}/patients`);
      setPatients(response.data);
    } catch (error) {
      console.error("Erro ao buscar pacientes:", error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !age || !disease) return alert("Preencha todos os campos!");

    const patientData = {
      name,
      age: parseInt(age),
      disease,
      priority
    };

    try {
      if (editingId) {
        await axios.put(`${API_URL}/patients/${editingId}`, patientData);
        setEditingId(null);
      } else {
        await axios.post(`${API_URL}/patients`, patientData);
      }
      clearForm();
      fetchPatients();
    } catch (error) {
      console.error("Erro ao salvar paciente:", error);
    }
  };

  const handleEdit = (patient) => {
    setEditingId(patient.id);
    setName(patient.name);
    setAge(patient.age);
    setDisease(patient.disease);
    setPriority(patient.priority);
  };

  const handleDeletePatient = async (id) => {
    try {
      await axios.delete(`${API_URL}/patients/${id}`);
      fetchPatients();
    } catch (error) {
      console.error("Erro ao deletar paciente:", error);
    }
  };

  const clearForm = () => {
    setName('');
    setAge('');
    setDisease('');
    setPriority(false);
    setEditingId(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hospital DC - Triagem de Pacientes</h1>
      </header>

      <main>
        <section className="form-section">
          <h2>{editingId ? 'Editar Cadastro' : 'Novo Cadastro'}</h2>
          <form onSubmit={handleSubmit}>
            <input 
              type="text" 
              placeholder="Nome do Paciente" 
              value={name} 
              onChange={(e) => setName(e.target.value)} 
            />
            <input 
              type="number" 
              placeholder="Idade" 
              value={age} 
              onChange={(e) => setAge(e.target.value)} 
            />
            <input 
              type="text" 
              placeholder="Sintomas/Doenca" 
              value={disease} 
              onChange={(e) => setDisease(e.target.value)} 
            />
            <label className="priority-label">
              <input 
                type="checkbox" 
                checked={priority} 
                onChange={(e) => setPriority(e.target.checked)} 
              />
              Prioridade
            </label>
            <div className="button-group">
              <button type="submit">{editingId ? 'Atualizar' : 'Cadastrar na Fila'}</button>
              {editingId && <button type="button" onClick={clearForm} className="cancel-btn">Cancelar</button>}
            </div>
          </form>
        </section>

        <section className="list-section">
          <h2>Fila de Atendimento</h2>
          <table>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Idade</th>
                <th>Sintomas</th>
                <th>Prioridade</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {patients.map((p) => (
                <tr key={p.id} className={p.priority ? 'priority-row' : ''}>
                  <td>{p.name}</td>
                  <td>{p.age}</td>
                  <td>{p.disease}</td>
                  <td>{p.priority ? 'Sim' : 'Nao'}</td>
                  <td>
                    <button onClick={() => handleEdit(p)} className="edit-btn">
                      Editar
                    </button>
                    <button onClick={() => handleDeletePatient(p.id)} className="delete-btn">
                      Dar Alta
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
}

export default App;
