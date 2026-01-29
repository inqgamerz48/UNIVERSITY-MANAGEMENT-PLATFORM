"use client";

import { useState } from "react";
import { api } from "@/lib/api";

export default function FacultyDashboard() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleAttendance = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        // Mock data for prototype
        const mockData = {
            subject_id: "mock-subject-id",
            date: new Date().toISOString().split('T')[0],
            records: [
                { student_id: "mock-student-1", status: "PRESENT" },
                { student_id: "mock-student-2", status: "ABSENT" }
            ]
        };

        try {
            await api.post("/operations/attendance/bulk", mockData);
            setMessage("✅ Attendance marked successfully!");
        } catch (err: any) {
            setMessage(`❌ Error: ${err.message}`);
        } finally {
            setLoading(false);
        }
    };

    const handleMarks = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        // Mock data
        const mockData = {
            student_id: "mock-student-1",
            subject_id: "mock-subject-id",
            exam_type: "FINAL",
            score: 85,
            max_score: 100
        };

        try {
            await api.post("/operations/marks", mockData);
            setMessage("✅ Marks uploaded successfully!");
        } catch (err: any) {
            setMessage(`❌ Error: ${err.message}`);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="p-8 space-y-8">
            <h1 className="text-3xl font-bold text-foreground">Faculty Dashboard</h1>
            {message && <div className="p-4 rounded bg-muted text-foreground">{message}</div>}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Attendance Card */}
                <div className="p-6 rounded-lg border border-border bg-card text-card-foreground shadow-sm">
                    <h2 className="text-xl font-semibold mb-4 text-primary">Mark Daily Attendance</h2>
                    <p className="text-sm text-muted-foreground mb-4">
                        Upload attendance for your assigned subjects.
                    </p>
                    <form onSubmit={handleAttendance} className="space-y-4">
                        <div className="grid gap-2">
                            <label className="text-sm font-medium">Subject ID</label>
                            <input className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background" placeholder="Mock Subject ID" disabled />
                        </div>
                        <button className="h-10 px-4 py-2 bg-primary text-primary-foreground hover:bg-primary/90 rounded-md w-full" disabled={loading}>
                            {loading ? "Processing..." : "Submit Attendance"}
                        </button>
                    </form>
                </div>

                {/* Marks Card */}
                <div className="p-6 rounded-lg border border-border bg-card text-card-foreground shadow-sm">
                    <h2 className="text-xl font-semibold mb-4 text-secondary-foreground">Upload Student Marks</h2>
                    <p className="text-sm text-muted-foreground mb-4">
                        Enter exam results for students.
                    </p>
                    <form onSubmit={handleMarks} className="space-y-4">
                        <div className="grid gap-2">
                            <label className="text-sm font-medium">Student ID</label>
                            <input className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background" placeholder="Mock Student ID" disabled />
                        </div>
                        <button className="h-10 px-4 py-2 bg-secondary text-secondary-foreground hover:bg-secondary/80 rounded-md w-full" disabled={loading}>
                            {loading ? "Processing..." : "Upload Marks"}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}
