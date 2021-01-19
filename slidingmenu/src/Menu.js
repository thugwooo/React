import React, {Component} from "react";
import "./Menu.css";

class Menu extends Component{
    render(){
        var visibility = "hide";

        if(this.props.menuVisibility){
            visibility = "show";
        }

        return(
            <div id="flyoutMenu"
            onMouseDown={this.props.handleMouseDown}
            className={visibility}>

                <h2><a herf="/">Home</a></h2>
                <h2><a herf="/">About</a></h2>
                <h2><a herf="/">Contact</a></h2>
                <h2><a herf="/">Search</a></h2>

            </div>
        );
    }
}

export default Menu;