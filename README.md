# Schools Technology Services (STS) Onboarding Knowledge Check

## Introduction

Schools Technology Services (STS) is a programme of policy work and digital services within the Department for Education’s Digital Data Technology Directorate. STS’ mission is to help schools save time and money when they plan and implement technology, by supporting them to increase their digital maturity.
There are two key services in STS: Digital Standards, which develops and publishes the [digital and technology standards for schools and colleges](https://www.gov.uk/guidance/meeting-digital-and-technology-standards-in-schools-and-colleges/updates) to guide schools to improve their technology, and Plan Technology For Your School (referred to as Plan Tech), which allows schools to assess their current digital maturity and receive tailored, trackable steps towards meeting the standards. My role is as a Junior Software Developer in Plan Tech.

Plan Tech is currently in public beta and has an ambitious plan for new features supporting collaboration between schools and multi-academy trusts. It is delivered by a full Agile team comprised of managed service provider personnel (contractors) with a small group of civil servants spread across disciplines. Contractors can be deployed, stood down or appointed to other teams within their provider’s contract at short notice, meaning that there are often new starters in the team who need to quickly familiarise themselves with the work landscape. Existing onboarding processes are largely administrative, with considerable onus placed on the new starter to educate themselves about the service.
The STS Onboarding Knowledge Check supports new starters in the Plan Tech team to build their knowledge of the portfolio, the service and their role within the team, using a combination of general service knowledge and discipline-specific questions. Tailored feedback will direct users to authoritative sources of information to help them fill knowledge gaps quickly. The knowledge check would ideally take place early in the user’s employment to direct and accelerate their learning.

## Design

![Prototype for quiz app](./static/assets/images/STS-knowledge-check-design.png)
*Fig. 1 Prototype screenshot with connected screens*

## Development

## Testing

## Documentation

### User documentation

### Technical documentation

This app uses Python v3.13.12, Flask v3.1.3 and pytest v9.0.2. For ease of installation the GOV.UK front-end framework is installed using compiled files, following [this installation documentation](https://frontend.design-system.service.gov.uk/install-using-precompiled-files/).

To install and run this project locally, first clone this repo:
```bash
git clone https://github.com/gilaineyo/if1_summative_AE2.git
```

Navigate to the project's root directory and install a virtual environment:
```bash
cd if1_summative_AE2
python -m venv venv
```
*Note: the command below is Windows-specific, for other operating systems refer to the [Python documentation on virtual environments](https://docs.python.org/3/library/venv.html)*.

Activate the virtual environment:
```bash
venv\Scripts\activate
```
Once active, install dependencies:
```bash
pip install flask
pip install pytest
```

## Evaluation
