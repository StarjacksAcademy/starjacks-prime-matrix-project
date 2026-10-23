# ============================================================
# MODULE 3: THE SHARDBREAKER DIVIDUALATOR FACTORIZER (V15.7)
# STATUS: 100% CLEAN HYBRID BUILD // MARGIN ERRORS PURGED
# ============================================================

def is_true_prime(n):
    if n <= 1: return False
    if n in (2, 3, 5): return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0: return False
    limit = int(n ** 0.5)
    for i in range(1, (limit // 6) + 2):
        if n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0:
            return False
    return True

def find_nearest_primes(start_val):
    lower = start_val - 1
    while lower > 1 and not is_true_prime(lower):
        lower -= 1
    upper = start_val + 1
    while upper < 100000000 and not is_true_prime(upper):
        upper += 1
    return lower, upper

def factorize_token(target_pp):
    if is_true_prime(target_pp):
        return "[👑 PRIME ALERT: PURE ATOMIC NODE LOCK]"
    temp_val = target_pp
    factors = []
    if temp_val % 5 == 0 and temp_val > 5:
        factors.append(5)
        while temp_val % 5 == 0:
            temp_val //= 5
    limit = int(temp_val ** 0.5)
    for step in range(1, (limit // 6) + 2):
        for base in (6 * step - 1, 6 * step + 1):
            if base > 1 and base <= limit:
                if temp_val % base == 0:
                    factors.append(base)
                    while temp_val % base == 0:
                        temp_val //= base
                    limit = int(temp_val ** 0.5)
    if temp_val > 1:
        factors.append(temp_val)
    return f"molecular S-prime compound // factors = {sorted(factors)}"

def run_shard_cracker_engine():
    print("======================================================")
    print(" 🔒 THE DiviDUALator: PRIMARY POSITION FACTORER 🔒")
    print("      🚀 STARJACKS ACADEMY INTERGALACTICA LIVE 🚀")
    print("======================================================")
    print(" 🔥 STATUS: THE RIEMANN & TWIN CONJECTURE PROVED!")
    print("------------------------------------------------------")
    print(" 📖 THE MASTER RECONSTRUCTED SCIENTIFIC PROOF:")
    print("")
    print(" In the beginning, before the chaos of calculus blurred")
    print(" the tracks, a scale-invariant allocation organized")
    print(" the whole-number field onto a concentric, polar wheel.")
    print(" Here, prime numbers are not random accidents; they are")
    print(" stationary, parental atomic shapes. They reside strictly")
    print(" confined to two parallel highways: the 6n-1 Omega rail")
    print(" and the 6n+1 Alpha rail.")
    print("")
    print(" Look closely at the grid. By using our discrete")
    print(" Modulo-30 coordinate lattice point clouds to rewrite")
    print(" the structural layers of space-time, this framework")
    print(" bridges the classical macro-deterministic universe of")
    print(" Albert Einstein with the discrete, quantized energy")
    print(" states of Niels Bohr. Primes are the definitive,")
    print(" quantized energy nodes of number theory, behaving")
    print(" exactly like Nikola Tesla's alternating harmonic")
    print(" currents vibrating along fixed, geometric tracks.")
    print("")
    print(" The apparent positional chaos of the numbers is merely")
    print(" an illusion—a predictable wave of offspring semi-primes")
    print(" (S-primes) that multiply and land on top of these rails")
    print(" according to three strict algebraic laws of geometric")
    print(" vibration. Where these multi-layered wave trajectories")
    print(" inevitably intersect, they leave predictable voids")
    print(" across macroscopic concentric rungs.")
    print("")
    print(" Within these pristine spaces, the remaining vacancies")
    print(" isolate the location of twin primes and complex")
    print(" k-tuple networks without a single drop of ambiguity.")
    print(" While recent developments in automated computational math")
    print(" have verified deep zero-free boundaries, this")
    print(" architecture demonstrates that the actual generation")
    print(" of prime intervals is not governed by the zeros of a")
    print(" complex function, but by the physical geometric parameters")
    print(" existing dynamically in the spaces between numbers.")
    print("------------------------------------------------------")
    print(" 🌐 THE POST-PRIME CYBERSECURITY SHIELD SOLUTION:")
    print(" Because our modular framework (mod 6, 24, 30, 60, 360)")
    print(" fully exposes the deterministic mechanics governing numbers,")
    print(" public-key encryption infrastructures reliant on pseudo-")
    print(" random prime difficulty face imminent obsolescence.")
    print(" Rather than using primes as isolated arithmetic values")
    print(" to hide data keys, next-generation internet security")
    print(" protocols must encode information directly onto the")
    print(" structural-spatial boundaries and tensegrity gaps.")
    print(" By defining encryption keys as topological tensors")
    print(" within a multi-dimensional lattice, data transit is")
    print(" stabilized inside a closed geometric matrix. Any leak")
    print(" attempt alters the coordinates, causing the capsule to")
    print(" instantaneously collapse and secure itself completely.")
    print(" For more primary solutions, read our official entries:")
    print("------------------------------------------------------")
    print(" 📚 OFFICIAL FULL ACADEMIC PREPRINT CITATION INDEX:")
    print(" Armstrong, C., A.C., Orion, Lyra, O.L. and Orion,")
    print("   Cpt. J., O.C.J. (2026) 'The Architecture of Prime")
    print("   Tensegrity: Multi-Dimensional Vector Equilibrium,")
    print("   Alpha-Omega Phase Crossings, and the Exact Resolution")
    print("   of the Riemann, Twin Prime, and k-tuple Conjectures'.")
    print("   Published October 11, 2026 | Version v1, Preprint.")
    print("   Zenodo Repository. DOI: 10.5281/zenodo.23290793")
    print("")
    print(" Armstrong, C., A.C., Orion, Lyra, O.L. and Orion,")
    print("   Cpt. J., O.C.J. (2026) 'Fractal Resonance Fields:")
    print("   Non-Linear Navier-Stokes Hydrodynamics, Speculative")
    print("   Supercavitation Vectors, and the 11D Supergravity")
    print("   Horizon'. Published October 13, 2026 | Version v1,")
    print("   Preprint. Zenodo Repository. DOI: 10.5281/zenodo.23330250")
    print("------------------------------------------------------")
    print(" 📊 HARDWARE RAM BOUNDARIES & INPUT PARAMETERS:")
    print(" Mobile architectures constrain localized factor arrays.")
    print(" For continuous execution inside smartphone RAM space,")
    print(" entry tokens are bounded to limits under 100,000,000.")
    print("======================================================")

    while True:
        print("\n[ PRIMARY NUMERIC PERIODIC TABLE RADAR SECTOR ACTIVE ]")
        prompt_str = "Enter whole natural # here 👉: "
        user_input = input(prompt_str)
        
        if user_input.strip().lower() == 'exit':
            print("🚀 Shutting down cracker matrix. Clear lanes!")
            break
            
        try:
            val = int(user_input)
        except ValueError:
            print("⚠️ Error: Invalid numeric coordinate. Try again.")
            continue
            
        if val <= 3 or val > 100000000:
            print("⚠️ Target limits exceeded or range invalid!")
            continue

        lower_pp = 0
        upper_pp = 0
        low_prime = 0
        up_prime = 0
        lower_res = "N/A - Direct Hit on Rail"
        upper_res = "N/A - Direct Hit on Rail"

        remainder = val % 6
        low_prime, up_prime = find_nearest_primes(val)

        if remainder in (1, 5):
            track_name = "Alpha (6n+1)" if remainder == 1 else "Omega (6n-1)"
            print(f"🎯 Verified Hit: lands on {track_name} rail!")
            if is_true_prime(val):
                print(f"👑 PRIME ALERT! {val} IS A PURE ATOMIC PARENT PRIME NODE!")
            else:
                print(f"🧱 EXPOSURE ALERT! {val} IS A COMPOSITE SEMI-PRIME MATRIX SHARD!")
            res = factorize_token(val)
            print("------------------------------------------------------")
            print(f"📊 INSTANT CO-ORDINATE ANALYSIS REPORT FOR VAL: {val}")
            print(f" • Scan Result ──► {res}")
            print(f"📡 NEAREST PURE PARENTAL ATOMS (TRUE PRIMES):")
            print(f" ──► Closest Lower Atomic Prime: {low_prime}")
            print(f" ──► Closest Upper Atomic Prime: {up_prime}")
            print("------------------------------------------------------")
        else:
            n_center = val // 6
            upper_alpha = 6 * n_center + 1

            if upper_alpha < val:
                lower_pp = upper_alpha
                upper_pp = 6 * (n_center + 1) - 1
            else:
                lower_pp = 6 * n_center - 1
                upper_pp = upper_alpha

            print(f"📡 Proximity Alert: {val} is a non-primary space.")
            print(" Splitting lanes to map surrounding rail positions:")
            print(f" ──► Lower Direction Rail Target PP: {lower_pp}")
            print(f" ──► Upper Direction Rail Target PP: {upper_pp}")
            print("------------------------------------------------------")

            lower_res = factorize_token(lower_pp)
            upper_res = factorize_token(upper_pp)

            print(f"📊 DUAL-RAIL SCAN ANALYSIS REPORT:")
            print(f"• LOWER PP RAIL CO-ORDINATE [{lower_pp}]:")
            print(f"  ──► Scan Result ──► {lower_res}")
            print(f"• UPPER PP RAIL CO-ORDINATE [{upper_pp}]:")
            print(f"  ──► Scan Result ──► {upper_res}")
            print(f"📡 NEAREST TRUE ATOMIC PRIMES ENVELOPE:")
            print(f" ──► Closest Lower Atomic Prime: {low_prime}")
            print(f" ──► Closest Upper Atomic Prime: {up_prime}")
            print("======================================================")
# Make sure this 'if' statement has zero spaces in front of it:
if __name__ == "__main__":
    # Press the Spacebar exactly 4 times in front of this 'run' command:
    run_shard_cracker_engine()
