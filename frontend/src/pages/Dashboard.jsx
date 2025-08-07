// File: frontend/src/pages/Dashboard.jsx
import { useEffect, useState } from 'react';
import { fetchLogReturns, fetchChangePoints } from '../api';
import PriceChart from '../components/PriceChart';
import EventHighlight from '../components/EventHighlight';

const Dashboard = () => {
  const [logReturns, setLogReturns] = useState([]);
  const [changePoints, setChangePoints] = useState([]);

  useEffect(() => {
    fetchLogReturns().then(res => setLogReturns(res.data));
    fetchChangePoints().then(res => setChangePoints(res.data));
  }, []);

  return (
    <div>
      <h2>Brent Oil Price Dashboard</h2>
      <PriceChart data={logReturns} />
      <EventHighlight events={changePoints} />
    </div>
  );
};

export default Dashboard;
