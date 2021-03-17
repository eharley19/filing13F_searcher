import React from 'react';
import '../App.css';
import { Button } from './Button';
import SearchBox from './SearchBox';
import './MainSection.css';

const divStyle = { float: 'left', padding: '20px', margin: '20px'};
const today = new Date();


function MainSection() {
    return (
        <>
            <div className='main-container'>
                <h1>COMPANY FINANCIAL HOLDINGS</h1>
                <p>Search 13F Filings by Company Name and Date</p>
                <SearchBox />
                <div style={divStyle}>
                <input type='date' className='date' defaultValue={today}></input>
                <input type='date' className='date' defaultValue={today}></input>
                </div>
                <Button buttonStyle='btn--outline' buttonSize='btn--large'>SEARCH</Button>     
            </div>
                     
        </>
    )
}
 
 export default MainSection
