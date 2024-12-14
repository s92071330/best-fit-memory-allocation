class BestFit:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks

    def allocate_memory(self, process_sizes):
        allocation = [-1] * len(process_sizes)  # Start with no allocations
        for i, size in enumerate(process_sizes):
            # Find the smallest block that fits
            best_index = min(
                (j for j, block in enumerate(self.memory_blocks) if block >= size),
                default=-1,
                key=lambda j: self.memory_blocks[j]
            )
            if best_index != -1:  # Allocate if a block is found
                allocation[i] = best_index
                self.memory_blocks[best_index] -= size  # Update block size
        return allocation


if __name__ == "__main__":
    print("========================================")
    print("       BEST FIT MEMORY ALLOCATION       ")
    print("========================================")
    print("\nWelcome! Please follow the instructions below.")
    print("\nStep 1: Enter process sizes as integers separated by spaces.")
    print("Example: 212 417 112 426\n")
    
    # User input
    process_sizes = list(map(int, input("> Enter process sizes separated by spaces: ").split()))
    memory_blocks = [100, 500, 200, 300, 600]
    
    # Perform memory allocation
    best_fit = BestFit(memory_blocks)
    allocation = best_fit.allocate_memory(process_sizes)
    
    # Display results
    print("\n========================================")
    print("           ALLOCATION RESULTS           ")
    print("========================================\n")
    print(f"Process Sizes:       {process_sizes}")
    print(f"Memory Allocation:   {allocation}")
    print(f"Updated Memory Blocks: {best_fit.memory_blocks}\n")
    print("Thank you for using the Best Fit Memory Allocation program!")
    print("========================================")
