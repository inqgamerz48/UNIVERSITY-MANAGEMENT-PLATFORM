"use client";

import { useState } from "react";
import { api } from "@/lib/api";

export default function StudentDashboard() {
    const [gpa, setGpa] = useState<number | null>(null);
    const [loading, setLoading] = useState(false);

    // Mock Student ID for prototype
    const STUDENT_ID = "mock-student-id";

    const fetchGPA = async () => {
        setLoading(true);
        try {
            const res = await api.get(`/academic/gpa/${STUDENT_ID}`);
            setGpa(res.sgpa);
        } catch (err) {
            alert("Failed to fetch GPA");
        } finally {
            setLoading(false);
        }
    };

    const downloadReport = (type: 'hall-ticket' | 'result') => {
        // Direct link to download PDF
        window.open(`http://localhost:8000/academic/reports/${type}/${STUDENT_ID}`, '_blank');
    };

    return (
        <div className="p-8 space-y-8">
            <h1 className="text-3xl font-bold text-foreground">Student Dashboard</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* GPA Card */}
                <div className="p-6 rounded-lg border border-border bg-card text-card-foreground shadow-sm flex flex-col items-center justify-center space-y-4">
                    <h2 className="text-xl font-semibold">Current SGPA</h2>
                    <div className="text-5xl font-bold text-primary">
                        {gpa !== null ? gpa : "-.--"}
                    </div>
                    <button
                        onClick={fetchGPA}
                        className="text-sm text-muted-foreground underline hover:text-foreground"
                        disabled={loading}
                    >
                        {loading ? "Calculating..." : "Refresh GPA"}
                    </button>
                </div>

                {/* Downloads */}
                <div className="col-span-2 p-6 rounded-lg border border-border bg-card text-card-foreground shadow-sm">
                    <h2 className="text-xl font-semibold mb-6">Downloads & Reports</h2>
                    <div className="grid grid-cols-2 gap-4">
                        <button
                            onClick={() => downloadReport('hall-ticket')}
                            className="h-24 rounded-md border-2 border-dashed border-muted hover:border-primary flex items-center justify-center text-lg font-medium transition-colors"
                        >
                            📄 Download Hall Ticket
                        </button>
                        <button
                            onClick={() => downloadReport('result')}
                            className="h-24 rounded-md border-2 border-dashed border-muted hover:border-primary flex items-center justify-center text-lg font-medium transition-colors"
                        >
                            📊 Download Result Card
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}
