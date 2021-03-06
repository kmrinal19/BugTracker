import React, { Component } from 'react'
import axios from 'axios'
import {connect} from 'react-redux'
// import { Redirect } from 'react-router-dom'
import { store } from '../index'
import {returnErrors} from '../actions/messages'
import { Loader ,Segment,Dimmer} from 'semantic-ui-react'

export class getauth extends Component {

    componentDidMount(){
        if (this.props.location.search) {
          console.log('inside')
          axios.get(`http://localhost:8000/BugTracker/auth${this.props.location.search}`)
                .then(res =>{
                  console.log(res.data)
                    store.dispatch({
                      type : 'LOGIN_SUCCESS',
                      payload : res.data
                    });
                    window.location.href='http://localhost:3000/'
                }
                ).catch(err => {returnErrors(err.response.data,err.response.status)
                  store.dispatch({
                    type : 'LOGIN_FAIL'
                  })
                }
                )
        }
      }

    render(){

        // // const queryString = require('query-string');
        // // const parsed = queryString.parse(this.props.location.search);
        // axios.get(`http://localhost:8000/BugTracker/auth${this.props.location.search}`)
        //     .then(res =>{
        //         console.log(res.data);
        //     }
        //     ).catch(err => {console.log(err)})
        return (
            <Segment className='fullscreen' style={{'background-color':'black','height':'-webkit-fill-available','width':'auto'}}>
            <Dimmer className='fullscreen' active>
              <Loader className='center' indeterminate>GOOD THINGS TAKE TIME</Loader>
            </Dimmer>
          </Segment>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        auth : state.auth
    }
}


export default connect(mapStateToProps)(getauth)
