import { useUser } from "@clerk/clerk-react";
import { Navigate, Outlet } from "react-router-dom";

// Role-Based Protection Wrapper
// "The Bridge": Uses Clerk User Data but validates Role logic.
// In Hybrid mode, we check publicMetadata, or fetch from our backend.
// For MVP Demo, we'll check publicMetadata or a role attribute.

export const ProtectedRoute = ({ allowedRoles }) => {
  const { isLoaded, isSignedIn, user } = useUser();

  if (!isLoaded) {
    return <div>Loading...</div>;
  }

  if (!isSignedIn) {
    return <Navigate to="/sign-in" replace />;
  }

  // LOGIC: Check role. 
  // For demo, we assume role is synced to publicMetadata OR matches a simple check.
  // If allowedRoles is null, just require auth.
  if (allowedRoles && allowedRoles.length > 0) {
      const userRole = user.publicMetadata?.role || "student"; // Default to student if missing
      
      if (!allowedRoles.includes(userRole)) {
          return <div>Access Denied: You are a {userRole || 'Guest'}, but need {allowedRoles.join(', ')}</div>;
      }
  }

  return <Outlet />;
};
