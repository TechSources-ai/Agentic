# appAgents/architecture.py
class ArchitectureAgent(BaseAgent):
    name = "architecture"
    def run(self, product, requirements):
        prompt = f"""
        You are a senior software architect.

        Design a production-ready software architecture for the following product.

        PRODUCT:
        {product}

        REQUIREMENTS:
        {requirements}

        Define:
        1. Technology stack
        2. Application architecture
        3. Database architecture
        4. Data models
        5. APIs
        6. Authentication
        7. Authorization
        8. Background jobs
        9. Caching
        10. Logging
        11. Monitoring
        12. Security
        13. Scalability
        14. Deployment architecture

        Explain important architectural decisions.
        """

        return self.llm.generate(prompt)