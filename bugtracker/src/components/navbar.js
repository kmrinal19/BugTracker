import React,{Component} from 'react';
import NavBarDesktop from './navbardesktop';
import NavBarMobile from './navbarmobile';
import {
    Responsive
  } from "semantic-ui-react";
class NavBar extends Component {
    state = {
      visible: false
    };
  
    handlePusher = () => {
      const { visible } = this.state;
  
      if (visible) this.setState({ visible: false });
    };
  
    handleToggle = () => this.setState({ visible: !this.state.visible });
  
    render() {
      const { leftItems, rightItems } = this.props;
      const { visible } = this.state;
  
      return (
        <div>
          <Responsive {...Responsive.onlyMobile}>
            <NavBarMobile
              leftItems={leftItems}
              onPusherClick={this.handlePusher}
              onToggle={this.handleToggle}
              rightItems={rightItems}
              visible={visible}
            >
              {/* <NavBarChildren>{children}</NavBarChildren> */}
            </NavBarMobile>
          </Responsive>
          <Responsive minWidth={Responsive.onlyTablet.minWidth}>
            <NavBarDesktop leftItems={leftItems} rightItems={rightItems} />
            {/* <NavBarChildren>{children}</NavBarChildren> */}
          </Responsive>
        </div>
      );
    }
  }
  
  export default NavBar;