import React from 'react'
import'./Journey.css'
export default function Journey() {
  return (
    <div className="journey">
        <span className="heading">My Journey</span>
        <div className="availablejourney">
            <span className="all">All</span>
            <span className='recent'>Kasauli</span>
        </div>
        <div className="trips">
            No trips planned yet!
        </div>
        <div className="bottom">
            <div className="title">
                Your current travel buddies
            </div>
            <div className="pic">
                <div className="items">
                    1
                </div>
                <div className="items">
                    1
                </div>
                <div className="items">
                    1
                </div>
                <div className="items">
                    1
                </div>
                <div className="items">
                    1
                </div>
            </div>
        </div>
    </div>
  )
}
