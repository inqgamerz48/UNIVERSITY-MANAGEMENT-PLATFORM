import { StatCard } from "@/components/dashboard/StatCard";
import { Users, BookOpen, GraduationCap, School } from "lucide-react";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-slate-50">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex mb-8">
        <h1 className="text-4xl font-bold text-slate-900">University Management Dashboard</h1>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4 w-full max-w-5xl">
        <StatCard
          label="Total Students Enrolled"
          value="2,847"
          icon={Users}
          trend={{ value: 156, label: "this semester", positive: true }}
        />
        <StatCard
          label="Active Courses"
          value="127"
          icon={BookOpen}
          trend={{ value: 8, label: "new this semester", positive: true }}
        />
        <StatCard
          label="Faculty Members"
          value="89"
          icon={GraduationCap}
          trend={{ value: 94, label: "teaching load", positive: true }}
        />
        <StatCard
          label="Departments"
          value="12"
          icon={School}
        />
      </div>

      <div className="mt-12 w-full max-w-5xl grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="p-6 bg-white rounded-xl shadow-sm border">
          <h3 className="text-lg font-semibold mb-4">Recent Activity</h3>
          <p className="text-muted-foreground">No recent activity.</p>
        </div>
        <div className="p-6 bg-white rounded-xl shadow-sm border">
          <h3 className="text-lg font-semibold mb-4">Quick Actions</h3>
          <div className="flex gap-2">
            <button className="px-4 py-2 bg-slate-900 text-white rounded-md text-sm">Add Student</button>
            <button className="px-4 py-2 border rounded-md text-sm hover:bg-slate-50">Create Course</button>
          </div>
        </div>
      </div>
    </main>
  );
}
