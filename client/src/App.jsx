
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Registrar los componentes de Chart.js que se utilizarán
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

import { useState } from 'react';
import axios from 'axios';

function App() {

  // ----------------- Codigo de los sensores ------------
  const [selectedSensor, setSelectedSensor] = useState("12");

  const handleSelectChange = (event) => {
    setSelectedSensor(event.target.value);
  };

  const handleButtonClick = (url) => {
    axios.post(url, {
      sensor: selectedSensor
    })
      .then(response => {
        console.log(response.data);
        // Manejar la respuesta aquí, como mostrar un mensaje de éxito
      })
      .catch(error => {
        console.error('Hubo un error!', error);
        // Manejar el error aquí, como mostrar un mensaje de error
      });
  };

  // ----------------- Graphic Interface -----------------
  const chartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June'],
    datasets: [
      {
        label: 'Revenue',
        backgroundColor: '#4e73df',
        borderColor: '#4e73df',
        data: [4500, 5300, 6250, 7800, 9800, 15000],
      },
    ],
  };

  const chartOptions = {
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: false,
        labels: {
          font: {
            weight: 'normal',
          },
        },
      },
      title: {
        display: true,
        text: 'Revenue',
        font: {
          weight: 'bold',
        },
      },
    },
    scales: {
      x: {
        ticks: {
          font: {
            weight: 'normal',
          },
        },
      },
      y: {
        ticks: {
          font: {
            weight: 'normal',
          },
        },
      },
    },
  };

  return (
    <>
      <nav className="navbar navbar-expand-lg fixed-top bg-secondary text-uppercase" id="mainNav">
        <div className="container"><a className="navbar-brand" href="#page-top">SMART BASE</a><button data-bs-toggle="collapse" data-bs-target="#navbarResponsive" className="navbar-toggler text-white bg-primary text-uppercase rounded" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i className="fa fa-bars"></i></button>
          <div className="collapse navbar-collapse" id="navbarResponsive">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item mx-0 mx-lg-1"></li>
              <li className="nav-item mx-0 mx-lg-1"></li>
              <li className="nav-item mx-0 mx-lg-1"></li>
            </ul>
          </div>
        </div>
      </nav>

      <header className="text-center text-white bg-primary masthead" style={{ background: 'rgb(194,43,125)', '--bs-primary': '#bc187a', '--bs-primary-rgb': '188,24,122' }}>
        <div className="container">
          <img className="img-fluid d-block mx-auto mb-5" src="./src/assets/img/OIP.png" style={{ borderStyle: 'none', borderRadius: '91px' }} alt="Logo" />
          <h1>DOME HOUSE</h1>
          <hr className="star-light" />
          <h2 className="fw-light mb-0">Automated - Safety - Efficiency</h2>
        </div>
      </header>

      <section id="portfolio" className="portfolio">
        <div className="container">
          <h2 className="text-uppercase text-center text-secondary">Sensores</h2>
          <hr className="star-dark mb-5" />
          <div className="row">
            <div className="col-md-6 col-lg-7">
              <form>
                <label className="form-label" style={{ marginTop: '10px', marginLeft: '5px' }}>
                  Seleccione Sensor:&nbsp;
                </label>
                <select className="form-select"
                  style={{ marginTop: '10px', marginLeft: '5px' }}
                  defaultValue="12"
                  onChange={handleSelectChange}>
                  <optgroup label="Sensores">
                    <option value="12">Temperatura</option>
                    <option value="13">Humedad</option>
                    <option value="14">Velocidad viento</option>
                    <option value="15">Luminosidad</option>
                    <option value="16">Calidad de aire</option>
                    <option value="17">Presión barométrica</option>
                  </optgroup>
                </select>
                <button
                  className="btn btn-primary"
                  type="button"
                  style={{
                    marginTop: '10px',
                    marginBottom: '5px',
                    marginRight: '5px',
                    marginLeft: '5px',
                    background: 'rgb(26,205,11)',
                    width: '94px',
                  }}
                  onClick={() => handleButtonClick('http://127.0.0.1:8000/api/on')}
                >
                  Encender
                </button>
                <button
                  className="btn btn-primary"
                  type="button"
                  style={{
                    marginTop: '10px',
                    marginRight: '5px',
                    marginBottom: '5px',
                    marginLeft: '5px',
                    width: '94px',
                    background: 'rgb(188,24,24)',
                  }}
                  onClick={() => handleButtonClick('http://127.0.0.1:8000/api/off')}
                >
                  Apagar
                </button>
                <button
                  className="btn btn-primary"
                  type="button"
                  style={{
                    marginTop: '10px',
                    marginBottom: '5px',
                    marginRight: '5px',
                    marginLeft: '5px',
                    background: 'rgb(22,118,187)',
                    width: '94px',
                  }}
                  onClick={() => handleButtonClick('http://127.0.0.1:8000/api/data')}
                >
                  Calcular
                </button>
                <button
                  className="btn btn-primary"
                  type="button"
                  style={{
                    marginTop: '10px',
                    marginRight: '5px',
                    marginBottom: '5px',
                    marginLeft: '5px',
                    width: '94px',
                  }}
                  onClick={() => handleButtonClick('http://127.0.0.1:8000/api/stats')}
                >
                  Graficar
                </button>
              </form>
            </div>
            <div className="col-md-6 col-lg-12 offset-lg-0">
              <div className="table-responsive">
                <table className="table">
                  <thead>
                    <tr>
                      <th>Promedio</th>
                      <th>Mediana</th>
                      <th>Desviación<br />Estandar</th>
                      <th>Máximo</th>
                      <th>Mínimo</th>
                      <th>Moda</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Cell 1</td>
                      <td>Cell 1</td>
                      <td>Cell 2</td>
                      <td>Cell 2</td>
                      <td>Cell 2</td>
                      <td>Cell 2</td>
                    </tr>
                    <tr></tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-8 offset-lg-0">
              <div className="card" style={{ marginTop: '10px', marginLeft: '0px', marginBottom: '10px' }}>
                <div className="card-body" style={{ marginTop: '10px', marginBottom: '11px' }}>
                  <div style={{ marginTop: '10px', marginLeft: '0px', marginBottom: '10px' }}>
                    <Bar data={chartData} options={chartOptions} />
                  </div>
                  <h4 className="card-title">Title</h4>
                  <p className="card-text">
                    Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in,
                    egestas eget quam. Donec id elit non mi porta gravida at eget metus.
                  </p>
                </div>
              </div>
            </div>
            <div className="col"></div>
          </div>
        </div>
      </section>

      <section id="contact">
        <div className="container">
          <h2 className="text-uppercase text-center text-secondary mb-0">Members</h2>
          <hr className="star-dark mb-5"></hr>
          <div className="row">
            <div className="col-lg-8 mx-auto">
              <form id="contactForm" name="sentMessage">
                <div></div>
                <div>
                  <div className="mb-0 form-floating pb-2"><small className="form-text text-danger help-block"></small></div>
                </div>
                <div>
                  <div className="mb-0 form-floating pb-2">
                    <p>201905884 - Santiago Julián Barrera Reyes<br></br>
                      201019694 - Henderson Migdo Baten Hernandez<br></br>
                      201801300 - Selim Idair Ergon Castillo<br></br>
                      210801521 - Jemima Solmaira Chavajay Quiejú<br></br>
                      202100229 - Giovanni Saul Concoha Cax<br></br>
                      202201405 - Johan Moises Cardona Rosales<br></br>
                      202204578 - Estiben Yair Lopez Leveron</p>
                  </div>
                </div>
                <div></div>
                <div id="success"></div>
                <div></div>
              </form>
            </div>
          </div>
        </div>
      </section>

      <div className="text-center text-white copyright py-4">
        <div className="container"><small>Copyright © SMARTH HOME 2024</small></div>
      </div>

    </>
  )
}

export default App
