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

exit 0
