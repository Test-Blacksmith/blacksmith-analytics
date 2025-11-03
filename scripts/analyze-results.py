#!/usr/bin/env python3
"""
Advanced analytics script for processing Blacksmith workflow results
This demonstrates technical depth beyond typical demos
"""

import json
import statistics
from datetime import datetime

def analyze_performance_data(metrics_files):
    """Statistical analysis of performance metrics"""
    durations = []
    
    for file in metrics_files:
        with open(file) as f:
            data = json.load(f)
            durations.append(data['duration_ms'])
    
    analysis = {
        'sample_size': len(durations),
        'mean': statistics.mean(durations),
        'median': statistics.median(durations),
        'stdev': statistics.stdev(durations) if len(durations) > 1 else 0,
        'min': min(durations),
        'max': max(durations),
        'range': max(durations) - min(durations),
    }
    
    # Coefficient of variation (CV) - key metric for predictability
    analysis['cv_percent'] = (analysis['stdev'] / analysis['mean'] * 100) if analysis['mean'] > 0 else 0
    
    # Percentiles
    sorted_durations = sorted(durations)
    analysis['p50'] = sorted_durations[len(sorted_durations)//2]
    analysis['p95'] = sorted_durations[int(len(sorted_durations)*0.95)]
    analysis['p99'] = sorted_durations[int(len(sorted_durations)*0.99)]
    
    return analysis

def generate_report(analysis):
    """Generate markdown report"""
    print("# Performance Analysis Report")
    print(f"\nGenerated: {datetime.now().isoformat()}")
    print(f"\n## Statistical Summary (n={analysis['sample_size']})")
    print(f"- Mean: {analysis['mean']:.0f}ms")
    print(f"- Median: {analysis['median']:.0f}ms")
    print(f"- Std Dev: {analysis['stdev']:.0f}ms")
    print(f"- CV: {analysis['cv_percent']:.1f}%")
    print(f"\n## Percentiles")
    print(f"- P50: {analysis['p50']:.0f}ms")
    print(f"- P95: {analysis['p95']:.0f}ms")
    print(f"- P99: {analysis['p99']:.0f}ms")
    print(f"\n## Range")
    print(f"- Min: {analysis['min']:.0f}ms")
    print(f"- Max: {analysis['max']:.0f}ms")
    print(f"- Range: {analysis['range']:.0f}ms")

if __name__ == '__main__':
    print("Analytics script ready for processing workflow metrics")
