// File: frontend/src/components/EventHighlight.jsx
import { useEffect, useState } from 'react';

const EventHighlight = ({ events }) => {
  return (
    <div>
      <h4>Detected Events</h4>
      <ul>
        {events.map((event, idx) => (
          <li key={idx}>
            <strong>{event.Date}:</strong> Change of {event.Change.toFixed(3)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventHighlight;
