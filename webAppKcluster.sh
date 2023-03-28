#!/bin/bash

# Variables
RESOURCE_GROUP="RG-Final-Project"
CLUSTER_NAME="webAppAKSCluster"
NODE_COUNT=1
KUBERNETES_VERSION="1.26.0"

# Create the resource group if it doesn't exist
az group create --name "$RESOURCE_GROUP" --location westeurope 

# Create the AKS cluster
az aks create \
  --resource-group "$RESOURCE_GROUP" \
  --name "$CLUSTER_NAME" \
  --node-count $NODE_COUNT \
  --generate-ssh-keys \
  --kubernetes-version "$KUBERNETES_VERSION"

# Get the cluster credentials
az aks get-credentials --resource-group "$RESOURCE_GROUP" --name "$CLUSTER_NAME"

# Verify the cluster connection
kubectl get nodes
