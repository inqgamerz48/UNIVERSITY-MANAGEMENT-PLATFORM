import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import { SignedIn, SignedOut, SignInButton, UserButton } from "@clerk/clerk-react";
import { ProtectedRoute } from './components/ProtectedRoute';
import './App.css'

function PublicPage() {
  return (
    <div>
      <h1>Public Page</h1>
      <p>Anyone can see this.</p>
      <SignedOut><SignInButton /></SignedOut>
      <SignedIn><UserButton /></SignedIn>
    </div>
  );
}

function StudentDashboard() {
  return <h1>🎓 Student Dashboard (Access Granted)</h1>;
}

function FacultyDashboard() {
  return <h1>👨‍🏫 Faculty Dashboard (Access Granted)</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        <nav>
          <Link to="/">Home</Link> | <Link to="/student">Student</Link> | <Link to="/faculty">Faculty</Link>
        </nav>

        <Routes>
          <Route path="/" element={<PublicPage />} />
          <Route path="/sign-in" element={<SignInButton />} />

          {/* Protected Routes */}
          <Route element={<ProtectedRoute allowedRoles={['student']} />}>
            <Route path="/student" element={<StudentDashboard />} />
          </Route>

          <Route element={<ProtectedRoute allowedRoles={['faculty']} />}>
            <Route path="/faculty" element={<FacultyDashboard />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
