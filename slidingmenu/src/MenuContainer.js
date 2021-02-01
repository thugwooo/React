import React, {Component} from "react";
import MenuButton from "./MenuButton";
import Menu from "./Menu";
class MenuContainer extends Component{
    constructor(props){
        super(props);
        this.state = {
            visible: false
        };
        this.toggleMenu = this.toggleMenu.bind(this);
        this.handleMouseDown = this.handleMouseDown.bind(this);
    }
    toggleMenu(){
        this.setState({
            visible: !this.state.visible
        });
    }
    handleMouseDown(e){
        this.toggleMenu();

        console.log("clicked");
        e.stopPropagation();
    }

    render(){
        return(
            <div>
                <MenuButton handleMouseDown={this.handleMouseDown}/>
                <Menu handleMouseDown={this.handleMouseDown}
                                        menuVisibility={this.state.visible}/>
                <div>
                    <p>쓰고싶은대로 쓰기</p>
                    <ul>
                        <li>강의자료 만들기</li>
                        <li>너무재밌당</li>
                        <li>매주</li>
                        <li>과제하는 기분이야</li>
                        <li>이상하다</li>
                        <li>나 수업은 다 들은거같은데</li>
                    </ul>
                </div>
            </div>
        );
    }
}
export default MenuContainer;

