import React from 'react';
import "./Sidebar.css";
import tent from "../../tent.jpeg";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faClipboardList, faUserGroup, faTrophy } from '@fortawesome/free-solid-svg-icons';

export default function Sidebar() {
  return (
    <div className="sidebar">
      <div className="user">
        <img src={tent} className="tentimg" alt="User" />
        <div className="name">
          <span>Ms. Gungun</span>
        </div>
      </div>
      <div className="list">
        <div className="item">
          <FontAwesomeIcon icon={faClipboardList} className='icon' />
          <span className='listspan'>My Journey</span>
        </div>
        <div className="item">
          <FontAwesomeIcon icon={faUserGroup} className='icon' />
          <span className='listspan'>My travel buddy</span>
        </div>
        <div className="item">
          <FontAwesomeIcon icon={faTrophy} className='icon' />
          <span className='listspan'>My collections</span>
        </div>
      </div>
    </div>
  );
}
