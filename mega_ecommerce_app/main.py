import argparse
from engine.context import initialize_app
from engine.workflow import CheckoutWorkflow

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=int, default=1, help="Error scenario to trigger (1, 2, or 3)")
    args = parser.parse_args()

    app_context = initialize_app()
    workflow = CheckoutWorkflow(app_context)
    
    print(f"\n=========================================")
    print(f"Starting E-Commerce Platform - Scenario {args.scenario}")
    print(f"=========================================\n")
    workflow.run_checkout_scenario(args.scenario)

if __name__ == '__main__':
    main()
