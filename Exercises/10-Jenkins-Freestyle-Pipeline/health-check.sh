#!/bin/bash

echo "===================================="
echo "       SYSTEM HEALTH CHECK"
echo "===================================="

echo ""
echo "Checking system hostname..."
hostname

echo ""
echo "Checking current date and time..."
date

echo ""
echo "Checking disk space..."
df -h /

echo ""
echo "Checking system uptime..."
uptime

echo ""
echo "===================================="
echo "       HEALTH CHECK COMPLETED"
echo "===================================="

echo "Health check exit status: 0"

exit 0