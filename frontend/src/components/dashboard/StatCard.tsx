import { cn } from "@/lib/utils";
import { LucideIcon } from "lucide-react";

interface StatCardProps {
    label: string;
    value: string | number;
    icon: LucideIcon;
    trend?: {
        value: number;
        label: string;
        positive: boolean;
    };
    className?: string;
}

export function StatCard({ label, value, icon: Icon, trend, className }: StatCardProps) {
    return (
        <div className={cn("rounded-xl border bg-card text-card-foreground shadow p-6", className)}>
            <div className="flex items-center justify-between space-y-0 pb-2">
                <p className="text-sm font-medium tracking-tight text-muted-foreground">
                    {label}
                </p>
                <Icon className="h-4 w-4 text-muted-foreground" />
            </div>
            <div className="flex flex-col">
                <div className="text-2xl font-bold">{value}</div>
                {trend && (
                    <p className={cn("text-xs flex items-center mt-1",
                        trend.positive ? "text-green-500" : "text-red-500"
                    )}>
                        {trend.positive ? "+" : ""}{trend.value}%
                        <span className="text-muted-foreground ml-1">
                            {trend.label}
                        </span>
                    </p>
                )}
            </div>
        </div>
    );
}
