import React from 'react'
import { Link } from "react-router-dom"
import { ProSidebar, Menu, MenuItem, SubMenu, SidebarContent } from 'react-pro-sidebar';
import { FaBookReader} from "react-icons/fa";


const CourseSidebar = () => {
    console.log(window.location.href.split('/')[4])
    const boolTeaching = window.location.href.split('/')[4] == 'teaching'

    return (

        <ProSidebar className = 'classSideBar'>
            <SidebarContent>
            <Menu iconShape="circle">
                <SubMenu title="Class Sidebar" icon={<FaBookReader />}>
                    <MenuItem>
                        Overview
                        <Link to="./overview" />
                    </MenuItem>
                    <MenuItem>
                        Curriculum
                        <Link to="./curriculum" />
                    </MenuItem>
                    <MenuItem>
                        Course Forum
                        <Link to="./forum" />
                    </MenuItem>
                    {boolTeaching
                    ?<React.Fragment>
                        <MenuItem>
                            Manage Quiz
                            <Link to="./quiz" />
                        </MenuItem>
                        <MenuItem>
                            Class Result
                            <Link to="./result" />
                        </MenuItem>
                    </React.Fragment>
                    :<MenuItem>
                        Take Quiz
                        <Link to="./quiz" />
                    </MenuItem>
                    }       
                </SubMenu>
            </Menu>
            </SidebarContent>
        </ProSidebar>
    )
}

export default CourseSidebar
