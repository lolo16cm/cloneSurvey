import {Navigate} from 'react-router-dom';
import { useAuthStore } from '../store/auth';

// children prop
const PrivateRoute = ({children}) => {
    // tale the obj/state of useAuthStore, then take the field of state: state.isLoggedIn, () call isLoggedIn immediatelly-> get().allUserData !== null,
    const loggedin = useAuthStore((state) => state.isLoggedIn)();
    
    return loggedin ? <>{children}</> : <Navigate to='/login/' />;
};

export default PrivateRoute;