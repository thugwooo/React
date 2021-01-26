import React, {Component} from "react";
import book1 from "./img/book1.png";
import book2 from "./img/book2.png";
import book3 from "./img/book3.png";
import book4 from "./img/book4.png";
import book5 from "./img/book5.png";
import book6 from "./img/book6.png";
import note1 from "./img/note1.png";
import supervise from "./img/supervise.png";

class Classes extends Component{

    render(){
        const imgStyle ={
            height: "280px",
            width : "440px"
        };
        const noteStyle = {
            heigth: "688",
            width : "485"
        };
        const superStyle = {
            height:"545",
            width :"504"
        };
        return(
            <div>
                <h2>교재</h2>
                <img src = {book1} style={imgStyle} alt="book1"/>
                <img src = {book2} style={imgStyle} alt="book2"/>
                <img src = {book3} style={imgStyle} alt="book3"/>
                <img src = {book4} style={imgStyle} alt="book4"/>
                <img src = {book5} style={imgStyle} alt="book5"/>
                <img src = {book6} style={imgStyle} alt="book6"/>
                <img src = {note1} style={noteStyle} alt="note1"/>
                <img src = {supervise} style={superStyle} alt="supervise"/>
            </div>
            
        );
    }
}
export default Classes;