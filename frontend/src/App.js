import logo from './logo.svg';
import './App.css';
import {
  createBrowserRouter,
  RouterProvider,
  Link,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <a href="/login">Login</a>,
  },
  {
    path: "/login",
    element: <Login/>
  }
]);

function App() {  
  return (
    <div className='app'>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
