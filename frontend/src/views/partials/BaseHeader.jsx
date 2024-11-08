import React, { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuthStore } from "../../store/auth";

function BaseHeader() {
    // const [cartCount, setCartCount] = useContext(CartContext);
    const [searchQuery, setSearchQuery] = useState("");
    const navigate = useNavigate();

    const handleSearchSubmit = () => {
        navigate(`/search/?search=${searchQuery}`);
    };

    const [isLoggedIn, user] = useAuthStore((state) => [state.isLoggedIn, state.user]);

    return (
        <div>
            <nav className="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
                <div className="container">
                    <Link className="navbar-brand" to="/">
                        Easy Survey
                    </Link>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className="nav-link" to="/pages/create">
                                    {" "}
                                    <i className="fas fa-solid fa-list-ul"></i> Create a Survey
                                </Link>
                            </li>

                            <li className="nav-item">
                                <Link className="nav-link" to="/pages/fill_out/">
                                    <i className="fas fa-clipboard-list"></i> Take the Survey
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/pages/result/">
                                    {" "}
                                    <i className="fas fa-solid fa-reply-all"></i> Result
                                </Link>
                            </li>
                        </ul>


                       
                        {isLoggedIn() === true ? (
                            <>
                                <Link to="/logout/" className="btn btn-primary ms-2" type="submit">
                                    Logout <i className="fas fa-usign-out-alt"></i>
                                </Link>
                            </>
                        ) : (
                            <>
                                {/* Login and register button */}
                                <Link to="/login/" className="btn btn-primary ms-2" type="submit">
                                    Login <i className="fas fa-sign-in-alt"></i>
                                </Link>
                                <Link
                                    to="/register/"
                                    className="btn btn-primary ms-2"
                                    type="submit"
                                >
                                    Register <i className="fas fa-user-plus"> </i>
                                </Link>
                            </>
                        )}
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default BaseHeader;
